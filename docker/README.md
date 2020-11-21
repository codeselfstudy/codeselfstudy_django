This project doesn't use Docker, but if you don't have Postgres installed, you can build a Docker container for it with this Dockerfile.

First build the Docker image:

```text
docker image build -f postgres.Dockerfile -t codeselfstudy_postgres .
```

Then run a container from the image:

```text
docker container run --rm \
    -p 5432:5432 \
    -v $(pwd)/pg:/var/lib/postgresql/data \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    --name codeselfstudy_postgres codeselfstudy_postgres
```

Django will then be able to connect to that Postgres database using the settings above. The data will be persisted in a local `pg` directory. Removing that directory will permanently delete the data.

If something else is already using port `5432` (like another instance of Postgres), then you can run the container on another port by changing the first `5432` in the command to something else, like `5431`. Update your `.env` file to match your chosen port.
