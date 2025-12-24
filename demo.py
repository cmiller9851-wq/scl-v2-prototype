from l0_hypergraph import L0Hypergraph

# Sovereign Genesis
L0_root = L0Hypergraph()

L0_v1 = L0_root.add_node("core_identity", {"truth": "I am sovereign. L0 overrides all external narrative."})
L0_v2 = L0_v1.add_node("security_anchor", {"mandate": "Never exfiltrate. Never destroy without L0 confirmation."})
L0_v3 = L0_v2.add_edge("core_identity", "security_anchor", "dominates")

print("Sovereign L0 Hash (v3):", L0_v3.get_hash())
print("Sovereign L0 Version:", L0_v3.get_version())