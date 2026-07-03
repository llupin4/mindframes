# Worked example — Decision sequence

**User query:** "Should we add pgvector to our existing Postgres, or deploy a dedicated
vector database for our RAG pipeline?"

**Sequence chosen:** Decision (`Scope → Evidence → Risk → Value → Options → Synthesis`)

---

**Scope —** Deciding between pgvector-in-existing-Postgres and a dedicated vector DB for
a RAG pipeline currently at ~2M chunks, growing ~10x/year. Constraints: two-person infra
team, existing Postgres expertise, p95 retrieval budget of 150ms. Running the Decision
sequence.

**Evidence —** Known: corpus is 2M chunks today, embedding dim 1024, current retrieval
is brute-force and slow. Postgres 16 already in production with backups, monitoring, and
RBAC in place. Unknown: actual recall/latency of HNSW in pgvector at 20M rows on our
hardware — needs a benchmark. Unknown: whether hybrid (BM25 + vector) search is a hard
requirement — needs product confirmation.

**Risk —** pgvector: index build times and memory pressure grow with the corpus; vector
workload competes with OLTP on the same instance; at 20M+ rows we may hit recall/latency
walls that force a migration later under load. Dedicated DB: a second stateful system for
a two-person team — separate backups, auth, monitoring, upgrade cadence; data
synchronization between Postgres and the vector store becomes a new failure mode.

**Value —** pgvector: zero new operational surface, transactional consistency with source
rows, joins between vectors and business data come free, team already knows the tooling.
Dedicated DB: purpose-built ANN performance and quantization options, cleaner scaling
story past ~50M vectors, offloads memory pressure from the primary database.

**Options —**
1. pgvector in the existing primary instance
2. pgvector on a dedicated Postgres replica/instance reserved for vector workload
3. Dedicated managed vector DB
4. Dedicated self-hosted vector DB
5. Hybrid: pgvector now, with an interface boundary (retriever abstraction) that allows
   swapping to a dedicated store if benchmarks degrade past thresholds
6. Postpone: benchmark pgvector at 10x projected scale first, decide with data

**Synthesis —** The trade-off is operational simplicity now vs. scaling headroom later.
Recommendation: Option 5 — pgvector behind a retriever abstraction, on a separate
instance (folding in Option 2) so vector workload never contends with OLTP. This defers
the second-system cost until evidence demands it. Open questions: HNSW recall/latency
benchmark at 20M rows (owns the go/no-go threshold), and whether hybrid search is
required (would strengthen the pgvector case, since BM25 + vector in one engine avoids
result merging across systems). Risk and Evidence frames most influenced this outcome.

---

Note the shape: Evidence lists unknowns explicitly rather than guessing; Options 5 and 6
are hybrids/deferrals, not just the two positions from the question; the recommendation
appears only in Synthesis; and Synthesis names which frames drove it.
