pg_hba.conf:
    file.managed:
        - name: /etc/postgresql/9.3/main/pg_hba.conf
        - source: salt://postgresql/pg_hba.conf
        - user: postgres
        - group: postgres
        - mode: 644
        - require:
            - pkg: postgresql-9.3

postgresql:
    pkg.installed:
        - name: postgresql-9.3
    service.running:
        - enabled: True
        - watch: 
            - file: /etc/postgresql/9.3/main/pg_hba.conf
        - require: 
            - pkg: postgresql-9.3

postgresql-9.3-dbg:
    pkg.installed:
        - name: postgresql-9.3-dbg

postgresql-server-dev-9.3:
    pkg.installed:
        - name: postgresql-server-dev-9.3
