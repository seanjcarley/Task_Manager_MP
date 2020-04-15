FROM gitpod/workspace-mysql
USER root

# Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

