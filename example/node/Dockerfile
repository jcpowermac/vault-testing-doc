FROM node:wheezy
RUN /usr/local/bin/npm install node-vault
RUN /usr/local/bin/npm install -g node-inspector
#RUN /usr/local/bin/npm install node-inspector
CMD node-inspector
EXPOSE 8080
EXPOSE 5828
COPY vault.js /root