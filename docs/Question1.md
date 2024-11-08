
---

### **3. Question 1: Data Validation (`question1.md`)**
```markdown
# Question 1: Data Validation

## Strategies
1. **Schema Validation**:
   - Validate data fields using tools like Pydantic or JSON Schema to ensure correct types and formats.
   - Example:
     ```python
     from pydantic import BaseModel

     class GameData(BaseModel):
         gameID: str
         team: str
         shotsOnGoal: int
     ```

2. **Range Checks**:
   - Ensure numerical values fall within acceptable ranges (e.g., `shotsOnGoal >= 0`).

3. **Referential Integrity**:
   - Ensure foreign keys like `player_id` exist in their reference datasets.

4. **Duplicate Removal**:
   - Remove duplicate rows during data cleaning.

5. **Automated Testing**:
   - Write unit tests to validate data integrity at each step.

## Why This Matters
- Ensures consistent, high-quality data.
- Prevents errors in downstream analytics or models.

