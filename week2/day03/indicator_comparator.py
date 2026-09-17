# indicator_comparator.py
# Mini CTI correlation engine: deduplicate and compare IOCs across threat feeds.

from collections import namedtuple

# A named tuple gives our IOCs shape without a full class
IOC = namedtuple("IOC", ["type", "value", "source"])


# ---------- Simulated Threat Feeds ----------
# In the real world, these come from APIs (Week 5) and JSON files (Week 4).
feed_a_raw = [
    "10.0.0.5", "192.168.1.100", "evil-c2.com", "10.0.0.5",   # duplicate on purpose
    "a1b2c3d4e5f6", "203.0.113.42"
]

feed_b_raw = [
    "10.0.0.5", "203.0.113.42", "evil-c2.com", "malware-host.net",
    "b2c3d4e5f6a1", "10.0.0.5"                                 # duplicate
]

feed_c_raw = [
    "10.0.0.5", "8.8.8.8", "malware-host.net", "e5f6a1b2c3d4"
]


# ---------- Step 1: Deduplicate Each Feed ----------
def dedupe(feed):
    """Convert a raw feed list to a set (removes duplicates)."""
    return set(feed)


# ---------- Step 2: Classify IOC Types (simple heuristic) ----------
def classify_ioc(value):
    """Very rough IOC type classifier."""
    if value.replace(".", "").isdigit():
        return "ip"
    if value.endswith((".com", ".net", ".org", ".io")):
        return "domain"
    if len(value) == 12 and all(c in "0123456789abcdef" for c in value):
        return "hash"
    return "unknown"


# ---------- Step 3: Build the Comparator ----------
class IndicatorComparator:
    def __init__(self, feeds):
        """
        feeds: dict of {feed_name: raw_list}
        """
        self.feeds = {name: dedupe(raw) for name, raw in feeds.items()}

    # ---- Aggregation ----
    def all_indicators(self):
        """Union of every indicator across every feed."""
        result = set()
        for feed in self.feeds.values():
            result |= feed
        return result

    def corroborated(self, min_feeds=2):
        """
        Return indicators seen in at least `min_feeds` different feeds.
        This is our confidence signal.
        """
        counts = {}
        for feed in self.feeds.values():
            for ioc in feed:
                counts[ioc] = counts.get(ioc, 0) + 1
        return {ioc for ioc, c in counts.items() if c >= min_feeds}

    def feed_counts(self):
        """How many feeds report each indicator."""
        counts = {}
        for feed in self.feeds.values():
            for ioc in feed:
                counts[ioc] = counts.get(ioc, 0) + 1
        return counts

    # ---- Pairwise comparisons ----
    def common_with(self, feed_name):
        """
        Return indicators shared between the given feed and all others.
        """
        if feed_name not in self.feeds:
            return set()
        target = self.feeds[feed_name]
        others = set()
        for name, feed in self.feeds.items():
            if name != feed_name:
                others |= feed
        return target & others

    def unique_to(self, feed_name):
        """Indicators that ONLY this feed reports."""
        if feed_name not in self.feeds:
            return set()
        others = set()
        for name, feed in self.feeds.items():
            if name != feed_name:
                others |= feed
        return self.feeds[feed_name] - others

    # ---- Scoring ----
    def confidence(self, ioc):
        """
        Simple confidence score: (number of feeds reporting) / (total feeds).
        """
        n = len(self.feeds)
        reporter_count = sum(1 for f in self.feeds.values() if ioc in f)
        return reporter_count / n if n else 0.0

    def ranked_indicators(self):
        """
        Return all indicators sorted by confidence descending.
        Each entry is an IOC namedtuple with a confidence score.
        """
        counts = self.feed_counts()
        ranked = []
        for ioc, count in counts.items():
            ranked.append(
                IOC(
                    type=classify_ioc(ioc),
                    value=ioc,
                    source=f"{count}/{len(self.feeds)} feeds"
                )
            )
        # Sort by number of feeds (highest first)
        ranked.sort(key=lambda x: int(x.source.split("/")[0]), reverse=True)
        return ranked

    # ---- Report ----
    def report(self):
        print("\n" + "=" * 66)
        print("🛰️  INDICATOR COMPARATOR — CTI CORRELATION REPORT")
        print("=" * 66)

        # Feed sizes
        print("\n📥 Feed sizes (after deduplication):")
        for name, feed in self.feeds.items():
            print(f"   {name}: {len(feed)} unique indicators")

        # Master list
        master = self.all_indicators()
        print(f"\n🌐 Total unique indicators across all feeds: {len(master)}")

        # Corroborated
        strong = self.corroborated(min_feeds=2)
        print(f"\n🔥 Corroborated (≥2 feeds): {len(strong)}")
        for ioc in sorted(strong):
            conf = self.confidence(ioc)
            print(f"   [conf {conf:.2f}] {classify_ioc(ioc):7} {ioc}")

        # Per-feed uniqueness
        print("\n🧭 Feed-exclusive indicators:")
        for name in self.feeds:
            uniq = self.unique_to(name)
            print(f"   {name} only: {sorted(uniq) if uniq else '—'}")

        # Ranked by confidence
        print("\n🏆 Ranked indicators by confidence:")
        for entry in self.ranked_indicators():
            print(f"   {entry.source:>10}  {entry.type:7}  {entry.value}")

        print("=" * 66)


# ---------- Demo ----------
def main():
    comparator = IndicatorComparator({
        "Feed-A": feed_a_raw,
        "Feed-B": feed_b_raw,
        "Feed-C": feed_c_raw
    })

    # Show raw vs deduped
    print("Raw feed A count:", len(feed_a_raw))
    print("Deduped feed A:    ", len(dedupe(feed_a_raw)), "unique")

    # Demonstration of set operations in the open
    a = dedupe(feed_a_raw)
    b = dedupe(feed_b_raw)

    print("\n--- Set Operations Between Feed A and Feed B ---")
    print("Union (A | B):", sorted(a | b))
    print("Intersection (A & B):", sorted(a & b))
    print("Difference (A - B):", sorted(a - b))
    print("Symmetric diff (A ^ B):", sorted(a ^ b))

    # Pairwise
    print("\n--- Pairwise ---")
    print("Common in Feed-A with others:", sorted(comparator.common_with("Feed-A")))
    print("Unique to Feed-C:", sorted(comparator.unique_to("Feed-C")))

    # Full report
    comparator.report()


if __name__ == "__main__":
    main()
