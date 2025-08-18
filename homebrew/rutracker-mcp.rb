class RutrackerMcp < Formula
  include Language::Python::Virtualenv

  desc "MCP server for RuTracker API"
  homepage "https://github.com/YOUR_USERNAME/rutracker-mcp"
  url "https://github.com/YOUR_USERNAME/rutracker-mcp/archive/v0.1.0.tar.gz"
  sha256 "YOUR_SHA256_HERE"
  license "MIT"

  depends_on "python@3.13"
  depends_on "uv" => :recommended

  def install
    virtualenv_install_with_resources
  end

  test do
    # Test that the command exists
    assert_match version.to_s, shell_output("#{bin}/rutracker-mcp --help")
  end
end
