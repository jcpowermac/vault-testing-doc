FROM node:wheezy
RUN /usr/local/bin/npm install node-vault && /usr/local/bin/npm install -g node-inspector
CMD node-inspector
EXPOSE 8080
EXPOSE 5828
COPY vault.js /root