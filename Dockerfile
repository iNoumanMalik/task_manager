# 1️⃣ Base Image
FROM python:3.11-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy requirements first (for caching)
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy project files
COPY . .

# 6️⃣ Expose port: This tells Docker that the container will listen on port 8000 at runtime.
EXPOSE 8000

# 7️⃣ Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# --host 0.0.0.0: Makes the app accessible from any network interface inside the container (not just localhost).
# --port 8000: Runs the server on port 8000, matching the EXPOSE instruction.