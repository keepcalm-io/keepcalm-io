{% if grains['os']=="Ubuntu" %}
/etc/apt/sources.list:
  file:
    - managed
    - source: salt://apt/sources.list

nginx-ppa-keys:
    cmd.run:
        - name: "apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C"
        - unless: 'apt-key list | grep C300EE8C'

chris-lea-ppa-keys:
    cmd.run:
        - name: "apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12"
        - unless: 'apt-key list | grep C7917B12'
{% endif %}