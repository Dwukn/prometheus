cmake_minimum_required(VERSION 3.20)
project(zeus VERSION 0.1.0 LANGUAGES CXX C)  # Add C language for proto.c

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Wayland and pkg-config
find_package(PkgConfig REQUIRED)
pkg_check_modules(WAYLAND_CLIENT REQUIRED wayland-client)

# Find wayland-scanner
find_program(WAYLAND_SCANNER wayland-scanner REQUIRED)

# Set protocol generation paths
set(PROTO_DIR "${CMAKE_CURRENT_SOURCE_DIR}/data")
set(PROTO_XML "${PROTO_DIR}/wlr-data-control-unstable-v1.xml")
set(PROTO_GEN_DIR "${CMAKE_BINARY_DIR}/generated")
file(MAKE_DIRECTORY ${PROTO_GEN_DIR})

# Output files
set(PROTO_HEADER "${PROTO_GEN_DIR}/wlr-data-control-unstable-v1-client-protocol.h")
set(PROTO_SOURCE "${PROTO_GEN_DIR}/wlr-data-control-unstable-v1-protocol.c")

# Custom command to generate Wayland protocol
add_custom_command(
    OUTPUT ${PROTO_HEADER} ${PROTO_SOURCE}
    COMMAND ${WAYLAND_SCANNER} client-header ${PROTO_XML} ${PROTO_HEADER}
    COMMAND ${WAYLAND_SCANNER} private-code ${PROTO_XML} ${PROTO_SOURCE}
    DEPENDS ${PROTO_XML}
    COMMENT "Generating Wayland protocol sources"
)

# Custom target for generation
add_custom_target(generate_wayland_protocol
    DEPENDS ${PROTO_HEADER} ${PROTO_SOURCE}
)

# Library for generated protocol
add_library(proto STATIC ${PROTO_SOURCE})
add_dependencies(proto generate_wayland_protocol)
target_include_directories(proto PUBLIC ${PROTO_GEN_DIR})
target_link_libraries(proto ${WAYLAND_CLIENT_LIBRARIES})

# zeusd executable
add_executable(zeusd src/main.cpp src/wayland_client.cpp)
target_include_directories(zeusd PRIVATE include)
target_link_libraries(zeusd proto ${WAYLAND_CLIENT_LIBRARIES})

# zeusctl executable
add_executable(zeusctl zeusctl/main.cpp)
