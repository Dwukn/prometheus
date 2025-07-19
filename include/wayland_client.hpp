#pragma once
#include <wayland-client.h>
#include "wlr-data-control-unstable-v1-client-protocol.h"
class WaylandClient {
public:
WaylandClient();
~WaylandClient();
bool connect();
void dispatch();
void roundtrip();
private:
static void registry_global(void *data, wl_registry *,
uint32_t name, const char *interface,
uint32_t version);
static void registry_global_remove(void *, wl_registry *, uint32_t) {}
static constexpr wl_registry_listener registry_listener_{
.global = registry_global,
.global_remove = registry_global_remove};
wl_display *display_ = nullptr;
wl_registry *registry_ = nullptr;
zwlr_data_control_manager_v1 *data_control_manager_ = nullptr;
};
