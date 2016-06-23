set(SRCS hello_world.F90)



# This step presumes "include $(PFUNIT)/include/base.mk" earlier in the makefile.
tests.x: testSuites.inc myTests.pf
         $(F90) -o $@ -I$(PFUNIT)/mod -I$(PFUNIT)/include \
                $(PFUNIT)/include/driver.F90 \
                ./*$(OBJ_EXT) $(LIBS) $(FFLAGS)




SOURCES = hello_world.F90


# This step presumes "include $(PFUNIT)/include/base.mk" earlier in the makefile.
tests.x: testSuites.inc myTests.pf
         $(F90) -o $@ -I$(PFUNIT)/mod -I$(PFUNIT)/include \
                $(PFUNIT)/include/driver.F90 \
                ./*$(OBJ_EXT) $(LIBS) $(FFLAGS)
