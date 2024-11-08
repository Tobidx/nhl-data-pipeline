# Question 2: Exception Handling

## Strategies
1. **API Retry Mechanisms**:
   - Implement retries with exponential backoff for transient errors.
   - Example:
     ```python
     for attempt in range(3):
         try:
             response = requests.get(url)
             response.raise_for_status()
         except requests.exceptions.RequestException:
             time.sleep(2 ** attempt)
     ```

2. **Graceful Failures**:
   - Log errors and continue processing other records.

3. **Monitoring and Alerts**:
   - Log failures and trigger alerts (e.g., email or Slack notifications).

## Why This Matters
- Ensures pipeline robustness in the face of transient or permanent API issues.
- Prevents complete pipeline failure due to a single error.
