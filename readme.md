# HomeMatic CCU Auto-Backup

This is a small script which periodically (at the moment: daily) fetches a backup of your CCU Device and uploads it into a S3 Storage (for example: Minio)
If the S3 upload fails, it will be saved into a local directory (currently the working directory, `/app`)


## Config

| ENV                  | Description                                                    | Required/Default |
|----------------------|----------------------------------------------------------------|------------------|
| `MINIO_HOST`         | S3 Endpoint of your storage server                             | required         |
| `MINIO_BUCKET`       | S3 Bucket to save into                                         | required         |
| `MINIO_ACCESS_KEY`   | S3 Access Key with write permissions into the given bucket     | required         |
| `MINIO_SECRET_KEY`   | S3 Secret key correspoding to the access key                   | required         |
| `HOMEMATIC_USERNAME` | Homematic User with backup permission (probably an Admin user) | required         |
| `HOMEMATIC_PASSWORD` | corresponding password                                         | required         |
| `HOMEMATIC_HOST`     | URL / Host to access the CCU Device                            | required         |


Or simply copy the `.env.example` file to `.env` and edit the values.

## Usage

Simple docker run: `docker run --env-file .env -d --name ccu3-backup n404/ccu3-backup`

Docker Compose Version:
```yaml
version: "3.6"
services:
  ccu3-backup:
    image: n404/ccu3-backup
    container_name: ccu3-backup
    restart: unless-stopped
    env_file:
      - .env
```

### Todo (Contributions are welcome)
- [ ] todo: before start: check for all necessary env variables (username hostname access token etc.)
- [ ] add an env variable for disabling S3 and use local storage by default
- [ ] add a useful logging library for displaying better time data in console logs
- [ ] add a config for the time schedule, when to back up


&copy; 2023 Trickfilm400