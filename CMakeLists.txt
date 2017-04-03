cmake_minimum_required(VERSION 3.5)  # Can probably use older
project (etest)
enable_language(Fortran)
enable_language(C)

# Where to look first for project cmake modules,
# before ${CMAKE_ROOT}/Modules/ is checked
set(CMAKE_MODULE_PATH
   ${CMAKE_SOURCE_DIR}/cmake
)

include(PreventInSourceBuild)
include(setup_rpath)

# -------------------------------------------
# Take location of ModelE from ModelE-Control
if (NOT DEFINED MODELE_ROOT)
    set(MODELE_ROOT $ENV{ECTL_PKG})
endif()

find_package(pFUnit REQUIRED)
include_directories(${PFUNIT_INCLUDE_DIR} ${PFUNIT_MOD_DIR})
list(APPEND ALL_LIBS ${PFUNIT_LIBRARY})

find_package(Everytrace REQUIRED)
include_directories(${EVERYTRACE_INCLUDE_DIR} ${EVERYTRACE_MOD_DIR})
list(APPEND ALL_LIBS ${EVERYTRACE_LIBRARY})

find_package(ModelE REQUIRED)
include_directories(${MODELE_INCLUDE_DIR})
list(APPEND ALL_LIBS ${MODELE_LIBRARY})

# -------------------------------------------

add_subdirectory(landice)
