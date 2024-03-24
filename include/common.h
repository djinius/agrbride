#pragma once

#include <cstdio>

#if defined(__DEBUG__) && !defined(__NOTRACE__)

#define TRACE(...) fprintf(stderr, __VA_ARGS__)
#define TRY(a, b) if(a) {} else { TRACE("%s:%d => Test " #a " failed.\n", __FILE__, __LINE__); goto b; }
#define CATCH(a) goto try_exception_end; a:
#define FINALLY try_exception_end:

#else

#define TRACE(...) 
#define TRY(a, b) if(a) {} else { goto b; }
#define CATCH(a) goto try_exception_end; a:
#define FINALLY try_exception_end:

#endif
