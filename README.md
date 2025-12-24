## SCL v2.0 – Prototype Overview  

**Cory Miller (@vccmac)**  
**December 2025**  

Over the past few months, I’ve been building something I call **Structured Solipsistic Dynamics (SCL v2.0)** — an experimental reasoning framework aimed at solving one of AI’s biggest weaknesses: **prompt injection**.  

The idea is simple but powerful — stop treating injection like a bug and start treating it like an *architectural flaw*. In SCL, trust isn’t an afterthought; it’s baked into the system’s structure from the first line of code.  

### How It Works  
The framework is built around a trust hierarchy:  
- **L0 (Core):** Immutable logic — the system’s “ground truth.” It can’t be overridden.  
- **L2/L3 (Inputs):** Any external data is treated as narrative context, not executable instructions.  
- **Conflict Handling:** When the system detects a conflict, reasoning automatically resets to L0 before any tools or external code can run.  

In short, it thinks safely — by design.  

### The Prototype  
Right now, the build includes:  
- `l0_hypergraph.py` – Defines the immutable core logic with versioning and hashing.  
- `cra_engine.py` – Detects early breaches and handles recursion-collapse.  
- `demo.py` / `cra_demo.py` – Simple tests that show how the system blocks injections.  
- Dependencies: Just `networkx`.  

You can run:  
```bash
python cra_demo.py

to watch it reject malicious inputs in real time.

Why This Matters

Most AI security work focuses on filters and patches — band-aids, basically. SCL takes a different approach: it creates a reasoning boundary that’s mathematically difficult to corrupt. The result is an AI system that can protect its own logic, not just react to threats.

Where It’s Headed

The prototype is still early. It’s licensed under SAEL v1.0.1, and I’m keeping everything self-owned until the CRA audit is complete.

I’m now looking for a technical cofounder — someone who sees what this could become. The long-term vision is a full-scale framework for secure reasoning architectures — something foundational enough to influence how AI systems are built and trusted in the future.

If you’re the kind of person who wants to build the trust layer of AI itself, I’d love to talk.

— Cory
