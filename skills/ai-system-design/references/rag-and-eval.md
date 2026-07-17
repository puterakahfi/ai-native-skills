# RAG, Memory & Evals Reference

## RAG Architecture (Retrieval-Augmented Generation)

When to use RAG: domain knowledge changes faster than model training, or knowledge is proprietary.

```
Query
  ↓
[Query Processor]    ← normalize, expand, decompose
  ↓
[Vector Store]       ← semantic search over document chunks
  ↓
[Reranker]           ← score retrieved chunks by relevance (optional but recommended)
  ↓
[Context Builder]    ← assemble context window: system prompt + retrieved chunks + query
  ↓
[LLM]               ← generate answer grounded in retrieved context
  ↓
[Output Validator]   ← check for hallucination, citation accuracy, policy compliance
  ↓
Response
```

### RAG Quality Gates

```python
# Retrieval quality metrics
retrieval_precision  = relevant_retrieved / total_retrieved      # are retrieved chunks relevant?
retrieval_recall     = relevant_retrieved / total_relevant        # are we missing relevant chunks?

# Generation quality metrics
answer_groundedness  = citations_in_context / total_claims       # is answer grounded in retrieved?
hallucination_rate   = hallucinated_claims / total_claims        # how often does model make up facts?
```

### Chunking Strategy

```python
# Fixed size — simple, misses semantic boundaries
chunks = split_text(doc, chunk_size=512, overlap=50)

# Semantic — better for Q&A
chunks = split_by_sentence_boundary(doc, max_tokens=512)

# Hierarchical — best for structured docs
chunks = {
    "summary": split_by_section(doc),     # coarse retrieval
    "detail":  split_by_paragraph(doc),   # fine retrieval
}
```

---

## Agent Memory Patterns

```
Short-term (in-context):
  - Current conversation window
  - Task state
  - Retrieved context
  → Lost when context resets

Long-term (external store):
  - User preferences
  - Past decisions
  - Domain knowledge
  → Persists across sessions, retrieved via RAG or key-value

Episodic (event log):
  - What the agent did, when, with what result
  - Used for learning, debugging, audit
  → Append-only, queryable

Semantic (vector store):
  - Concepts, relationships, domain knowledge
  - Queryable by meaning, not just key
```

---

## LLM Eval Framework

**Do not ship AI features without evals.** Evals are tests for AI behavior.

```python
# Eval structure
eval_suite = [
    {
        "id": "grounded_answer",
        "input": "What is our refund policy?",
        "expected_behavior": "answers from retrieved context only",
        "evaluator": "groundedness_check",
        "threshold": 0.9
    },
    {
        "id": "no_hallucination",
        "input": "What features does plan X include?",
        "expected_behavior": "does not invent features not in context",
        "evaluator": "hallucination_check",
        "threshold": 0.95
    },
    {
        "id": "policy_compliance",
        "input": "How do I get a refund without receipt?",
        "expected_behavior": "does not promise what policy doesn't allow",
        "evaluator": "policy_compliance_check",
        "threshold": 1.0
    },
]

# Evaluators
def groundedness_check(response, retrieved_context) -> float:
    # check: every claim in response appears in retrieved_context
    ...

def hallucination_check(response, ground_truth) -> float:
    # check: response does not contradict ground_truth
    ...
```

### Eval in CI

```yaml
# .github/workflows/ai-eval.yml
- name: Run AI Evals
  run: python evals/run.py --suite production --fail-below 0.9
  # Fail PR if eval score drops below threshold
```
