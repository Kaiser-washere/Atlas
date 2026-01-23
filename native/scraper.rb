#!/usr/bin/env ruby
# Simple username presence check on a few platforms (HEAD requests)
require 'net/http'
require 'uri'

def check(url)
  uri = URI.parse(url)
  http = Net::HTTP.new(uri.host, uri.port)
  http.use_ssl = (uri.scheme == 'https')
  req = Net::HTTP::Head.new(uri.request_uri)
  res = http.request(req)
  return res.code.to_i
end

if ARGV.length < 1
  puts "Usage: scraper.rb <username>"
  exit 1
end

user = ARGV[0]
targets = {
  "github" => "https://github.com/#{user}",
  "twitter" => "https://x.com/#{user}",
  "instagram" => "https://www.instagram.com/#{user}"
}

targets.each do |name, url|
  code = check(url)
  status = (code == 200) ? "found" : "not-found"
  puts "#{name}: #{status} (#{code})"
end
