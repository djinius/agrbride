SRCDIR:=./srcs
BINDIR:=./bin
INCLUDEDIR:=./include

CC:=gcc
CXX:=g++
LD:=g++
CFLAGS:=-g -Wall -Wno-unused-result -I${INCLUDEDIR} -IC:\msys64\mingw64\include\SDL2
OFLAGS:=-O2 -fno-omit-frame-pointer
LFLAGS:=-L C:\msys64\mingw64\lib -lSDL2main -lSDL2_image -lSDL2 

CXXSRCS:=agrbride.cpp layer.cpp window.cpp button.cpp
OBJLIST:=${CXXSRCS:.cpp=.o}
OBJS=$(foreach O,$(OBJLIST),$(BINDIR)/$(O))
PROG:=agrbride.exe

ifeq ($(build_mode),release)
	CFLAGS+=$(OFLAGS)
else
ifeq ($(build_mode),release)
	CFLAGS+=-D__DEBUG__ $(OFLAGS)
else
	CFLAGS+=-D__DEBUG__
endif
endif

ifeq ($(notrace),yes)
	CFLAGS+=-D__NOTRACE__
endif

ifeq ($(console_mode),windows)
	CFLAGS+=-DWIN32
	LDFLAGS=-Wl,-subsystem,windows $(LFLAGS)
else
	LDFLAGS=-lmingw32 $(LFLAGS)
endif

CXXFLAGS:=${CFLAGS}

.PHONY: all

all: ${PROG}

${PROG}: ${OBJS}
	${LD} ${OBJS} -o $@ ${LDFLAGS}

test: ${PROG}
	gdb ${PROG}

clean:
	rm -Rf ${OBJS} ${PROG}

${BINDIR}/%.o: ${SRCDIR}/%.cpp ${INCLUDEDIR}/*.h Makefile
	${CXX} ${CXXFLAGS} -c $< -o $@
