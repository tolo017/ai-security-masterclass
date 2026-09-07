is_authenticated = True
is_suspicious = True
risk_score = 0

if not is_authenticated:
    decision = "BLOCK"
elif not is_suspicious:
    decision = "REVIEW"
elif not is_authenticated and risk_score >= 50:
    decision = "BLOCK"
elif not is_suspicious and risk_score >= 20:
    decision = "REVIEW"
else:
    decision = "ALLOW"
    
print(decision)
