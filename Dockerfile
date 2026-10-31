# Local preview of the Jekyll blog. Gems live in /deps inside the image,
# so the repo's Windows Gemfile.lock is left untouched.
FROM ruby:3.2-slim
RUN apt-get update && apt-get install -y --no-install-recommends build-essential git \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /deps
COPY Gemfile Gemfile.lock jekyll-text-theme.gemspec ./
ENV BUNDLE_GEMFILE=/deps/Gemfile
RUN bundle lock --add-platform x86_64-linux && bundle install --jobs 4
WORKDIR /site
EXPOSE 4000 35729
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--livereload", "--force_polling", "--destination", "/tmp/_site"]
