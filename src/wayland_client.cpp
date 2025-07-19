#include "wayland_client.hpp"
#include <cstdio>
#include <cstring>          // <-- NEW

WaylandClient::WaylandClient() = default;
WaylandClient::~WaylandClient() {
    if (data_control_manager_)
        zwlr_data_control_manager_v1_destroy(data_control_manager_);
    if (registry_)
        wl_registry_destroy(registry_);
    if (display_)
        wl_display_disconnect(display_);
}

bool WaylandClient::connect() {
    display_ = wl_display_connect(nullptr);
    if (!display_) {
        std::fprintf(stderr, "Cannot connect to Wayland display\n");
        return false;
    }

    registry_ = wl_display_get_registry(display_);
    wl_registry_add_listener(registry_, &registry_listener_, this);
    roundtrip();
    if (!data_control_manager_) {
        std::fprintf(stderr,
                     "Compositor lacks zwlr_data_control_manager_v1\n");
        return false;
    }
    return true;
}

void WaylandClient::registry_global(void* data, wl_registry* reg,
                                    uint32_t name, const char* iface,
                                    uint32_t ver) {
    auto self = static_cast<WaylandClient*>(data);
    if (std::strcmp(iface, zwlr_data_control_manager_v1_interface.name) == 0) { // std:: removed
        self->data_control_manager_ = static_cast<zwlr_data_control_manager_v1*>(
            wl_registry_bind(reg, name,
                             &zwlr_data_control_manager_v1_interface,
                             1));
    }
}

void WaylandClient::dispatch() { wl_display_dispatch(display_); }
void WaylandClient::roundtrip() { wl_display_roundtrip(display_); }
