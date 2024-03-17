SRCDIR:=./srcs
BINDIR:=./bin
INCLUDEDIR:=./include

CC:=gcc
CXX:=g++
LD:=g++
CFLAGS:=-g -Wall -Wno-unused-result -I${INCLUDEDIR} -IC:\msys64\mingw64\include\SDL2
CXXFLAGS:=${CFLAGS}
OFLAGS:=-O2 -fno-omit-frame-pointer
LDFLAGS:=-L C:\msys64\mingw64\lib -lmingw32 -lSDL2main -lSDL2_image -lSDL2 

CXXSRCS:=agrbride.cpp
OBJLIST:=${CXXSRCS:.cpp=.o}
OBJS=$(foreach O,$(OBJLIST),$(BINDIR)/$(O))
PROG:=agrbride.exe

ifeq ($(build_mode),release)
	CFLAGS += $(OFLAGS)
	CXXFLAGS += $(OFLAGS)
endif

.PHONY: all

all: ${PROG}

${PROG}: ${OBJS}
	${LD} ${OBJS} -o $@ ${LDFLAGS}

test: ${PROG}
	./${PROG}

clean:
	rm -Rf ${OBJS} ${PROG}

${BINDIR}/%.o: ${SRCDIR}/%.cpp Makefile
	${CXX} ${CXXFLAGS} -c $< -o $@

echo:
	echo $(OBJS)