#ifndef TURTLE_H_INCLUDED
# define TURTLE_H_INCLUDED

#include <stdint.h>

int spawn_turtle(void);
void turtle_fd(int32_t);
void turtle_bk(int32_t);
void turtle_lt(int32_t);
void turtle_rt(int32_t);
void turtle_goto(int32_t, int32_t);
void turtle_pu(void);
void turtle_pd(void);
void turtle_exit(void);

#endif  // !defined(TURTLE_H_INCLUDED)