# Question 3: Securing Sensitive Keys

## Strategies
1. **Environment Variables**:
   - Store sensitive keys in environment variables.
   - Example:
     ```bash
     export API_KEY=your_api_key
     ```
     Access in Python:
     ```python
     import os
     api_key = os.getenv("API_KEY")
     ```

2. **Secrets Management**:
   - Use tools like AWS Secrets Manager or HashiCorp Vault to securely store and retrieve secrets.

3. **Avoid Hardcoding**:
   - Never hardcode keys in your code or commit them to version control.

4. **Encryption**:
   - Encrypt sensitive files if they need to be shared.

## Why This Matters
- Protects sensitive credentials from leaks or unauthorized access.
- Complies with best practices for secure development.
