# HomeMatic CCU Auto-Backup

This is a small script which periodically (at the moment: daily) fetches a backup of your CCU Device and uploads it into a S3 Storage (for example: Minio)
If the S3 upload fails, it will be saved into a local directory (currently the working directory, `/app`)


## Config

| ENV                          | Description                                                              | Required/Default |
|------------------------------|--------------------------------------------------------------------------|------------------|
| `MINIO_HOST`                 | S3 Endpoint of your storage server                                       | required         |
| `MINIO_BUCKET`               | S3 Bucket to save into                                                   | required         |
| `MINIO_ACCESS_KEY`           | S3 Access Key with write permissions into the given bucket               | required         |
| `MINIO_SECRET_KEY`           | S3 Secret key corresponding to the access key                            | required         |
| `HOMEMATIC_USERNAME`         | Homematic User with backup permission (probably an Admin user)           | required         |
| `HOMEMATIC_PASSWORD`         | corresponding password                                                   | required         |
| `HOMEMATIC_HOST`             | URL / Host to access the CCU Device                                      | required         |
| `CRON_MONITORING_URL_START`  | URL which will be called upon job start (format: `http://...`)           | optional         |
| `CRON_MONITORING_URL_OK`     | URL which will be called upon job (format: `http://...`)                 | optional         |
| `CRON_MONITORING_URL_FAILED` | URL which will be called upon job error (format: `http://...`)           | optional         |
| `RUN_ONCE`                   | `true` if no schedule should be used. running one and then exits process | optional         |


Or simply copy the `.env.example` file to `.env` and edit the values.

## Usage

The Dockerimage with the `latest` tag is available for `amd64` and `arm64`.

Simple docker run: `docker run --env-file .env -d --name ccu3-backup n404/ccu3-backup`

See on [DockerHub](https://hub.docker.com/r/n404/ccu3-backup).

Docker Compose Version:
```yaml
services:
  ccu3-backup:
    image: n404/ccu3-backup
    container_name: ccu3-backup
    restart: unless-stopped
    env_file:
      - .env
```

### external schedule

If you want to use an external schedule like crontab / kubernetes jobs, set the environment variable `RUN_ONCE` to `true`.
The process will execute the backup and then stop.

### Todo (Contributions are welcome)
- [ ] todo: before start: check for all necessary env variables (username hostname access token etc.)
- [ ] add an env variable for disabling S3 and use local storage by default
- [ ] add a useful logging library for displaying better time data in console logs
- [ ] add a config for the time schedule, when to back up
- [ ] Update packages with `== -> >=` and `pip install --upgrade -r requirements.txt` and `pip freeze > requirements.txt`

&copy; 2023-2025 Trickfilm400