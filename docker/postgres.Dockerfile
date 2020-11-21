FROM postgres:12-alpine
RUN apk --no-cache add pspg
COPY init.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
