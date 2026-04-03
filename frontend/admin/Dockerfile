FROM nginx:alpine

# Remove default config (optional but clean)
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx config
COPY k8s-nginx.conf /etc/nginx/nginx.conf

# Copy admin HTML
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
