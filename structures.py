# MIT License
# 
# Copyright (c) 2010-2019 NVIDIA Corporation
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

from ctypes import Structure, CFUNCTYPE
from ctypes import c_uint32, c_void_p, c_int

class NVENC_RECT(Structure):
    _fields_ = [
        ('left', c_uint32),
        ('top', c_uint32),
        ('right', c_uint32),
        ('bottom', c_uint32)
        ]

class NV_ENC_CREATE_INPUT_BUFFER(Structure):
    _fields_ = [
        ('version', c_uint32),
        ('width', c_uint32),
        ('height', c_uint32),
        ('memoryHeap', c_uint32),
        ('bufferFmt', c_uint32),
        ('reserved', c_uint32),
        ('inputBuffer', c_void_p),
        ('pSysMemBuffer', c_void_p),
        ('reserved1', c_uint32 * 57),
        ('reserved2', c_void_p * 63)
        ]

class NV_ENC_CREATE_BITSTREAM_BUFFER(Structure):
    _fields_ = [
        ('version', c_uint32),
        ('size', c_uint32),
        ('memoryHeap', c_uint32),
        ('reserved', c_uint32),
        ('bitstreamBuffer', c_uint32),
        ('bitstreamBufferPtr', c_void_p),
        ('reserved1', c_uint32 * 58),
        ('reserved2', c_void_p * 64)
        ]

class NV_ENC_OPEN_ENCODE_SESSION_EX_PARAMS(Structure):
    _fields_ = [
        ('version', c_uint32),
        ('deviceType', c_uint32),
        ('device', c_void_p),
        ('reserved', c_void_p),
        ('apiVersion', c_uint32),
        ('reserved1', c_uint32 * 253),
        ('reserved2', c_void_p * 64)
        ]

class NVENC_EXTERNAL_ME_HINT_COUNTS_PER_BLOCKTYPE(Structure):
    _fields_ = [
        ('numCandsPerBlk', c_uint32),
        ('reserved1', c_uint32 * 3),
        ]

class NV_ENC_INITIALIZE_PARAMS(Structure):
    _pack_ = 1
    _fields_ = [
        ('version', c_uint32),
        ('encodeGUID', GUID),
        ('presetGUID', GUID),
        ('encodeWidth', c_uint32),
        ('encodeHeight', c_uint32),
        ('darWidth', c_uint32),
        ('darHeight', c_uint32),
        ('frameRateNum', c_uint32),
        ('frameRateDen', c_uint32),
        ('enableEncodeAsync', c_uint32),
        ('enablePTD', c_uint32),
        ('reservedBitFields', c_uint32),
        ('privDataSize', c_uint32),
        ('privData', c_void_p),
        ('encodeConfig', c_void_p),
        ('maxEncodeWidth', c_uint32),
        ('maxEncodeHeight', c_uint32),
        ('maxMEHintCountsPerBlock', NVENC_EXTERNAL_ME_HINT_COUNTS_PER_BLOCKTYPE * 2),
        ('reserved', c_uint32 * 289),
        ('reserved2', c_void_p * 64),
        ]

class NV_ENCODE_API_FUNCTION_LIST(Structure):
    _fields_ = [
        ('version', c_uint32),
        ('reserved', c_uint32),
        ('nvEncOpenEncodeSession', CFUNCTYPE(c_int, c_void_p, c_uint32, POINTER(c_void_p))),
        ('nvEncGetEncodeGUIDCount', CFUNCTYPE(c_int, c_void_p, POINTER(c_uint32))),
        ('nvEncGetEncodeProfileGUIDCount', c_void_p),
        ('nvEncGetEncodeProfileGUIDs', c_void_p),
        ('nvEncGetEncodeGUIDs', CFUNCTYPE(c_int, c_void_p, c_void_p, c_uint32, POINTER(c_uint32))),
        ('nvEncGetInputFormatCount', c_void_p),
        ('nvEncGetInputFormats', c_void_p),
        ('nvEncGetEncodeCaps', c_void_p),
        ('nvEncGetEncodePresetCount', c_void_p),
        ('nvEncGetEncodePresetGUIDs', c_void_p),
        ('nvEncGetEncodePresetConfig', c_void_p),
        ('nvEncInitializeEncoder', CFUNCTYPE(c_int, c_void_p, POINTER(NV_ENC_INITIALIZE_PARAMS))),
        ('nvEncCreateInputBuffer', CFUNCTYPE(c_int, c_void_p, POINTER(NV_ENC_CREATE_INPUT_BUFFER))),
        ('nvEncDestroyInputBuffer', c_void_p),
        ('nvEncCreateBitstreamBuffer', CFUNCTYPE(c_int, c_void_p, POINTER(NV_ENC_CREATE_BITSTREAM_BUFFER))),
        ('nvEncDestroyBitstreamBuffer', c_void_p),
        ('nvEncEncodePicture', c_void_p),
        ('nvEncLockBitstream', c_void_p),
        ('nvEncUnlockBitstream', c_void_p),
        ('nvEncLockInputBuffer', c_void_p),
        ('nvEncUnlockInputBuffer', c_void_p),
        ('nvEncGetEncodeStats', c_void_p),
        ('nvEncGetSequenceParams', c_void_p),
        ('nvEncRegisterAsyncEvent', c_void_p),
        ('nvEncUnregisterAsyncEvent', c_void_p),
        ('nvEncMapInputResource', c_void_p),
        ('nvEncUnmapInputResource', c_void_p),
        ('nvEncDestroyEncoder', c_void_p),
        ('nvEncInvalidateRefFrames', c_void_p),
        ('nvEncOpenEncodeSessionEx', CFUNCTYPE(c_int, POINTER(NV_ENC_OPEN_ENCODE_SESSION_EX_PARAMS), POINTER(c_void_p))),
        ('nvEncRegisterResource', c_void_p),
        ('nvEncUnregisterResource', c_void_p),
        ('nvEncReconfigureEncoder', c_void_p),
        ('reserved1', c_void_p),
        ('nvEncCreateMVBuffer', c_void_p),
        ('nvEncDestroyMVBuffer', c_void_p),
        ('nvEncRunMotionEstimationOnly', c_void_p),
        ('reserved2', c_void_p * 281)
        ]