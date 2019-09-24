# MIT License
# 
# Copyright (c) 2008-2019 Company for Advanced Supercomputing Solutions LTD
# Author: Mordechai Botrashvily (support@cass-hpc.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

from ctypes import c_uint32

class NV_ENC_DEVICE_TYPE:
    NV_ENC_DEVICE_TYPE_DIRECTX          = c_uint32(0x0)
    NV_ENC_DEVICE_TYPE_CUDA             = c_uint32(0x1)
    NV_ENC_DEVICE_TYPE_OPENGL           = c_uint32(0x2)

class NV_ENC_BUFFER_FORMAT:
    NV_ENC_BUFFER_FORMAT_UNDEFINED                       = c_uint32(0x00000000)
    NV_ENC_BUFFER_FORMAT_NV12                            = c_uint32(0x00000001)
    NV_ENC_BUFFER_FORMAT_YV12                            = c_uint32(0x00000010)
    NV_ENC_BUFFER_FORMAT_IYUV                            = c_uint32(0x00000100)
    NV_ENC_BUFFER_FORMAT_YUV444                          = c_uint32(0x00001000)
    NV_ENC_BUFFER_FORMAT_YUV420_10BIT                    = c_uint32(0x00010000)
    NV_ENC_BUFFER_FORMAT_YUV444_10BIT                    = c_uint32(0x00100000)
    NV_ENC_BUFFER_FORMAT_ARGB                            = c_uint32(0x01000000)
    NV_ENC_BUFFER_FORMAT_ARGB10                          = c_uint32(0x02000000)
    NV_ENC_BUFFER_FORMAT_AYUV                            = c_uint32(0x04000000)
    NV_ENC_BUFFER_FORMAT_ABGR                            = c_uint32(0x10000000)
    NV_ENC_BUFFER_FORMAT_ABGR10                          = c_uint32(0x20000000)
    NV_ENC_BUFFER_FORMAT_U8                              = c_uint32(0x40000000)