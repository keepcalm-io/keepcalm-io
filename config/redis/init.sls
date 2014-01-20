redis.conf:
    file.managed:
        - name: /etc/redis/redis.conf
        - source: salt://redis/redis.conf
        - require:
            - pkg: redis-server