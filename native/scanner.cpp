#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <netdb.h>
#include <fcntl.h>  

bool check_port(const std::string& host, int port, int timeout_ms = 800) {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) return false;

    sockaddr_in addr{};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);

    // Resolve host
    hostent* he = gethostbyname(host.c_str());
    if (!he) { close(sock); return false; }
    memcpy(&addr.sin_addr, he->h_addr_list[0], he->h_length);

    // Set non-blocking
    int flags = fcntl(sock, F_GETFL, 0);
    fcntl(sock, F_SETFL, flags | O_NONBLOCK);

    int res = connect(sock, (sockaddr*)&addr, sizeof(addr));
    if (res < 0 && errno != EINPROGRESS) { close(sock); return false; }

    fd_set wfds;
    FD_ZERO(&wfds);
    FD_SET(sock, &wfds);
    timeval tv{ timeout_ms / 1000, (timeout_ms % 1000) * 1000 };

    res = select(sock + 1, nullptr, &wfds, nullptr, &tv);
    bool open = false;
    if (res > 0) {
        int err; socklen_t len = sizeof(err);
        if (getsockopt(sock, SOL_SOCKET, SO_ERROR, &err, &len) == 0 && err == 0) open = true;
    }
    close(sock);
    return open;
}

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "Usage: scanner <host> <ports_comma>\n";
        return 1;
    }
    std::string host = argv[1];
    std::string ports_str = argv[2];

    std::vector<int> ports;
    size_t start = 0;
    while (true) {
        size_t pos = ports_str.find(',', start);
        std::string token = (pos == std::string::npos) ? ports_str.substr(start) : ports_str.substr(start, pos - start);
        if (!token.empty()) ports.push_back(std::stoi(token));
        if (pos == std::string::npos) break;
        start = pos + 1;
    }

    for (int p : ports) {
        bool is_open = check_port(host, p);
        std::cout << p << (is_open ? " open\n" : " closed\n");
    }
    return 0;
}
