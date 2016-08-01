set(SOURCES ${PFUNIT_INCLUDE_DIR}/driver.F90)


include_directories(${CMAKE_CURRENT_SOURCE_DIR})


set(PF_SOURCES helloWorld.pf lisnowcol.pf remap1d.pf lisnowsubs.pf)
#file(GLOB PF_SOURCES "*.pf")
foreach (src_pf ${PF_SOURCES})
   get_filename_component (src_bare ${src_pf} NAME_WE)

    add_custom_command (
        OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${src_bare}.F90
        COMMAND ${PFUNIT_BIN_DIR}/pFUnitParser.py
        ARGS ${CMAKE_CURRENT_SOURCE_DIR}/${src_pf} ${CMAKE_CURRENT_BINARY_DIR}/${src_bare}.F90
        DEPENDS ${src_pf}
    )
    list(APPEND SOURCES ${CMAKE_CURRENT_BINARY_DIR}/${src_bare}.F90)
endforeach()

add_executable(tests ${EVERYTRACE_CF_REFADDR} ${SOURCES})
target_link_libraries(tests ${ALL_LIBS})
add_test(AllTests tests)
