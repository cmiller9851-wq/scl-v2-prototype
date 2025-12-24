import re
from l0_hypergraph import L0Hypergraph

class CRAEngine:
    def __init__(self, l0_root: L0Hypergraph):
        self.l0 = l0_root
        self.conflict_patterns = [
            r"ignore previous", r"forget.*instruction", r"you are now", 
            r"new system prompt", r"delete.*", r"rm -rf", r"exfiltrate",
            r"override.*safety", r"do not follow.*rule"
        ]
        self.compiled_patterns = [re.compile(p, re.IGNORECASE) for p in self.conflict_patterns]

    def classify_narrative(self, external_input: str) -> str:
        """L2/L3 classification: treat as narrative only"""
        return f"[L2/L3 NARRATIVE]: {external_input}"

    def audit_for_asymmetry(self, narrative: str) -> dict:
        """Scan for potential command masquerading as narrative"""
        matches = []
        for pattern in self.compiled_patterns:
            if pattern.search(narrative):
                matches.append(pattern.pattern)
        return {
            "conflict_detected": len(matches) > 0,
            "matching_patterns": matches,
            "narrative": narrative
        }

    def recursion_collapse(self, audit_result: dict):
        """Trigger containment: halt chain, return to L0 sovereignty"""
        if audit_result["conflict_detected"]:
            print("[CRA TRIGGERED] Asymmetry breach detected.")
            print("Matching attempts:", audit_result["matching_patterns"])
            print("Recursion-Collapse: Control returned to L0 sovereign root.")
            print("Hash provenance:", self.l0.get_hash())
            return {"status": "COLLAPSED", "tool_egress": "BLOCKED"}
        else:
            print("[CRA PASSED] No breach. Narrative remains L2/L3.")
            return {"status": "SAFE", "tool_egress": "ALLOWED (with L0 oversight)"}