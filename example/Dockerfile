FROM centos

RUN mkdir -p /opt/hashicorp/vault/bin/ && \
    mkdir -p /var/opt/hashicorp/vault/ && \
    mkdir -p /opt/hashicorp/vault/etc/policies

COPY ansible.hcl /opt/hashicorp/vault/etc/policies
COPY vault.hcl /opt/hashicorp/vault/etc/

RUN yum install -y unzip git wget vim epel-release && \
    yum install -y python-pip python-devel

RUN pip install hvac

WORKDIR /opt/hashicorp/vault/bin/
ADD https://releases.hashicorp.com/vault/0.6.0/vault_0.6.0_linux_amd64.zip /opt/hashicorp/vault/bin/vault.zip

RUN unzip vault.zip

CMD ./vault server -config ../etc/vault.hcl 
EXPOSE 8200
