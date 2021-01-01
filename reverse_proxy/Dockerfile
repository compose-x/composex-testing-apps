FROM public.ecr.aws/nginx/nginx

RUN groupadd -r app -g 1042 && useradd -u 1042 -r -g app -m -d /app -s /sbin/nologin -c "App user" app && chmod 755 /app
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 443
