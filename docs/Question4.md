# Question 4: Profiling and Optimization

## Strategies
1. **Profiling Tools**:
   - Use Python's `cProfile` or `line_profiler` to identify bottlenecks.
   - Example:
     ```bash
     python -m cProfile src/dag_pipeline.py
     ```

2. **Optimize Hotspots**:
   - Focus on high-impact areas (e.g., large loops or I/O operations).

3. **Parallelization**:
   - Use threading or multiprocessing for API calls or data processing.

4. **Caching**:
   - Cache results for frequently repeated API calls.

## Why This Matters
- Improves pipeline efficiency and reduces execution time.
- Ensures scalability for larger datasets or higher workloads.
