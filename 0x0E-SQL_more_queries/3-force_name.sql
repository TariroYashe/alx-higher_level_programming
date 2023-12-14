--script that creates the table force_name on your MySQL server
USE hbtn_0d_2;

-- Create force_name table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
