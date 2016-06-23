cmake_minimum_required(VERSION 3.5)  # Can probably use older
project (etest)
enable_language(Fortran)

# Where to look first for project cmake modules,
# before ${CMAKE_ROOT}/Modules/ is checked
set(CMAKE_MODULE_PATH
   ${CMAKE_SOURCE_DIR}/cmake
)

include(PreventInSourceBuild)
include(setup_rpath)

# -------------------------------------------
# Take location of ModelE from Ectl
if (NOT DEFINED MODELE_ROOT)
    set(MODELE_ROOT $ENV{ECTL_PKG})
endif()

find_package(ModelE REQUIRED)
include_directories(${MODELE_INCLUDE_DIR})
list(APPEND ALL_LIBS ${MODELE_LIBRARY})

find_package(pFUnit REQUIRED)
include_directories(${PFUNIT_INCLUDE_DIR} ${PFUNIT_MOD_DIR})
list(APPEND ALL_LIBS ${PFUNIT_LIBRARY})

# -------------------------------------------

add_subdirectory(landice)
