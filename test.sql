CREATE TABLE site_visits (
  id INT PRIMARY KEY,
  ip VARCHAR(45),
  user_agent TEXT,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  page_url VARCHAR(255)
);