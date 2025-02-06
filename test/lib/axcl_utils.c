#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#include "axcl_rt_device.h"


typedef struct _TEST_DATA_T {
    char * pData;
    int nSize;
}TEST_DATA_T;

static char g_data[1024] = {0};
static int  g_size = 0;

AXCL_EXPORT int test_input(TEST_DATA_T *pData) {
    if (pData) {
        if (pData->pData) {
            memcpy(g_data, pData->pData, pData->nSize);
            g_size = pData->nSize;

            printf("pData=%p, size=%d, pData[0]=0x%02x, pData[%d]=0x%02x\n", pData->pData, pData->nSize, pData->pData[0], pData->nSize-1, pData->pData[pData->nSize-1]);
        }
    }

    return AXCL_SUCC;
}

AXCL_EXPORT int test_output(TEST_DATA_T *pData) {
    if (pData) {
        pData->pData = &g_data[0];
        pData->nSize = g_size;
    }
    return AXCL_SUCC;
}