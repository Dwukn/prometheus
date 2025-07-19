#include "wayland_client.hpp"
#include <csignal>
#include <cstdio>
volatile sig_atomic_t running = 1;
void on_sigint(int) { running = 0; }
int main() {
    std::signal(SIGINT, on_sigint);
    WaylandClient client;
    if (!client.connect()) return 1;
    std::puts("zeusd: connected to compositor, wlr-data-control available.");
    while (running) client.dispatch();
    std::puts("zeusd: goodbye.");
    return 0;
}
