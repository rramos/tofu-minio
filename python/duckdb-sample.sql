-- DuckDB SQL script to create a table with data from MinIO

CREATE SECRET secret1 (
    TYPE S3,
    KEY_ID 'ACCESS_KEY',
    SECRET 'SECRET_KEY',
    REGION 'us-east-1',
    ENDPOINT 'localhost:9000',
    URL_STYLE 'path', 
    USE_SSL false

);

SELECT * FROM 's3://state-terraform-s3/sample_data.csv';

