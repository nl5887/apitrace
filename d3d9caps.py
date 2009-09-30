##########################################################################
#
# Copyright 2008-2009 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

"""d3d9caps.h"""

from windows import *
from d3d9types import *

D3DVS20CAPS = Flags(DWORD, [
    "D3DVS20CAPS_PREDICATION",
])

D3DVSHADERCAPS2_0 = Struct("D3DVSHADERCAPS2_0", [
    (D3DVS20CAPS, "Caps"),
    (INT, "DynamicFlowControlDepth"),
    (INT, "NumTemps"),
    (INT, "StaticFlowControlDepth"),
])

D3DPS20CAPS = Flags(DWORD, [
    "D3DPS20CAPS_ARBITRARYSWIZZLE",
    "D3DPS20CAPS_GRADIENTINSTRUCTIONS",
    "D3DPS20CAPS_PREDICATION",
    "D3DPS20CAPS_NODEPENDENTREADLIMIT",
    "D3DPS20CAPS_NOTEXINSTRUCTIONLIMIT",
])

D3DPSHADERCAPS2_0 = Struct("D3DPSHADERCAPS2_0", [
    (D3DPS20CAPS, "Caps"),
    (INT, "DynamicFlowControlDepth"),
    (INT, "NumTemps"),
    (INT, "StaticFlowControlDepth"),
    (INT, "NumInstructionSlots"),
])

D3DCAPS = Flags(DWORD, [
    "D3DCAPS_READ_SCANLINE",
])

D3DCAPS2 = Flags(DWORD, [
    "D3DCAPS2_FULLSCREENGAMMA",
    "D3DCAPS2_CANCALIBRATEGAMMA",
    "D3DCAPS2_RESERVED",
    "D3DCAPS2_CANMANAGERESOURCE",
    "D3DCAPS2_DYNAMICTEXTURES",
    "D3DCAPS2_CANAUTOGENMIPMAP",
    "D3DCAPS2_CANSHARERESOURCE",
])

D3DCAPS3 = Flags(DWORD, [
    "D3DCAPS3_RESERVED",
    "D3DCAPS3_ALPHA_FULLSCREEN_FLIP_OR_DISCARD",
    "D3DCAPS3_LINEAR_TO_SRGB_PRESENTATION",
    "D3DCAPS3_COPY_TO_VIDMEM",
    "D3DCAPS3_COPY_TO_SYSTEMMEM",
])


D3DPRESENT_INTERVAL = Flags(DWORD, [
    "D3DPRESENT_INTERVAL_DEFAULT",
    "D3DPRESENT_INTERVAL_ONE",
    "D3DPRESENT_INTERVAL_TWO",
    "D3DPRESENT_INTERVAL_THREE",
    "D3DPRESENT_INTERVAL_FOUR",
    "D3DPRESENT_INTERVAL_IMMEDIATE",
])

D3DCURSORCAPS = Flags(DWORD, [
    "D3DCURSORCAPS_COLOR",
    "D3DCURSORCAPS_LOWRES",
])

D3DDEVCAPS = Flags(DWORD, [
    "D3DDEVCAPS_EXECUTESYSTEMMEMORY",
    "D3DDEVCAPS_EXECUTEVIDEOMEMORY",
    "D3DDEVCAPS_TLVERTEXSYSTEMMEMORY",
    "D3DDEVCAPS_TLVERTEXVIDEOMEMORY",
    "D3DDEVCAPS_TEXTURESYSTEMMEMORY",
    "D3DDEVCAPS_TEXTUREVIDEOMEMORY",
    "D3DDEVCAPS_DRAWPRIMTLVERTEX",
    "D3DDEVCAPS_CANRENDERAFTERFLIP",
    "D3DDEVCAPS_TEXTURENONLOCALVIDMEM",
    "D3DDEVCAPS_DRAWPRIMITIVES2",
    "D3DDEVCAPS_SEPARATETEXTUREMEMORIES",
    "D3DDEVCAPS_DRAWPRIMITIVES2EX",
    "D3DDEVCAPS_HWTRANSFORMANDLIGHT",
    "D3DDEVCAPS_CANBLTSYSTONONLOCAL",
    "D3DDEVCAPS_HWRASTERIZATION",
    "D3DDEVCAPS_PUREDEVICE",
    "D3DDEVCAPS_QUINTICRTPATCHES",
    "D3DDEVCAPS_RTPATCHES",
    "D3DDEVCAPS_RTPATCHHANDLEZERO",
    "D3DDEVCAPS_NPATCHES",
])

D3DPMISCCAPS = Flags(DWORD, [
    "D3DPMISCCAPS_MASKZ",
    "D3DPMISCCAPS_CULLNONE",
    "D3DPMISCCAPS_CULLCW",
    "D3DPMISCCAPS_CULLCCW",
    "D3DPMISCCAPS_COLORWRITEENABLE",
    "D3DPMISCCAPS_CLIPPLANESCALEDPOINTS",
    "D3DPMISCCAPS_CLIPTLVERTS",
    "D3DPMISCCAPS_TSSARGTEMP",
    "D3DPMISCCAPS_BLENDOP",
    "D3DPMISCCAPS_NULLREFERENCE",
    "D3DPMISCCAPS_INDEPENDENTWRITEMASKS",
    "D3DPMISCCAPS_PERSTAGECONSTANT",
    "D3DPMISCCAPS_FOGANDSPECULARALPHA",
    "D3DPMISCCAPS_SEPARATEALPHABLEND",
    "D3DPMISCCAPS_MRTINDEPENDENTBITDEPTHS",
    "D3DPMISCCAPS_MRTPOSTPIXELSHADERBLENDING",
    "D3DPMISCCAPS_FOGVERTEXCLAMPED",
    "D3DPMISCCAPS_POSTBLENDSRGBCONVERT",
])

D3DLINECAPS = Flags(DWORD, [
    "D3DLINECAPS_TEXTURE",
    "D3DLINECAPS_ZTEST",
    "D3DLINECAPS_BLEND",
    "D3DLINECAPS_ALPHACMP",
    "D3DLINECAPS_FOG",
    "D3DLINECAPS_ANTIALIAS",
])

D3DPRASTERCAPS = Flags(DWORD, [
    "D3DPRASTERCAPS_DITHER",
    "D3DPRASTERCAPS_ZTEST",
    "D3DPRASTERCAPS_FOGVERTEX",
    "D3DPRASTERCAPS_FOGTABLE",
    "D3DPRASTERCAPS_MIPMAPLODBIAS",
    "D3DPRASTERCAPS_ZBUFFERLESSHSR",
    "D3DPRASTERCAPS_FOGRANGE",
    "D3DPRASTERCAPS_ANISOTROPY",
    "D3DPRASTERCAPS_WBUFFER",
    "D3DPRASTERCAPS_WFOG",
    "D3DPRASTERCAPS_ZFOG",
    "D3DPRASTERCAPS_COLORPERSPECTIVE",
    "D3DPRASTERCAPS_SCISSORTEST",
    "D3DPRASTERCAPS_SLOPESCALEDEPTHBIAS",
    "D3DPRASTERCAPS_DEPTHBIAS",
    "D3DPRASTERCAPS_MULTISAMPLE_TOGGLE",
])

D3DPCMPCAPS = Flags(DWORD, [
    "D3DPCMPCAPS_NEVER",
    "D3DPCMPCAPS_LESS",
    "D3DPCMPCAPS_EQUAL",
    "D3DPCMPCAPS_LESSEQUAL",
    "D3DPCMPCAPS_GREATER",
    "D3DPCMPCAPS_NOTEQUAL",
    "D3DPCMPCAPS_GREATEREQUAL",
    "D3DPCMPCAPS_ALWAYS",
])

D3DPBLENDCAPS = Flags(DWORD, [
    "D3DPBLENDCAPS_ZERO",
    "D3DPBLENDCAPS_ONE",
    "D3DPBLENDCAPS_SRCCOLOR",
    "D3DPBLENDCAPS_INVSRCCOLOR",
    "D3DPBLENDCAPS_SRCALPHA",
    "D3DPBLENDCAPS_INVSRCALPHA",
    "D3DPBLENDCAPS_DESTALPHA",
    "D3DPBLENDCAPS_INVDESTALPHA",
    "D3DPBLENDCAPS_DESTCOLOR",
    "D3DPBLENDCAPS_INVDESTCOLOR",
    "D3DPBLENDCAPS_SRCALPHASAT",
    "D3DPBLENDCAPS_BOTHSRCALPHA",
    "D3DPBLENDCAPS_BOTHINVSRCALPHA",
    "D3DPBLENDCAPS_BLENDFACTOR",
    "D3DPBLENDCAPS_SRCCOLOR2",
    "D3DPBLENDCAPS_INVSRCCOLOR2",
])

D3DPSHADECAPS = Flags(DWORD, [
    "D3DPSHADECAPS_COLORGOURAUDRGB",
    "D3DPSHADECAPS_SPECULARGOURAUDRGB",
    "D3DPSHADECAPS_ALPHAGOURAUDBLEND",
    "D3DPSHADECAPS_FOGGOURAUD",
])

D3DPTEXTURECAPS = Flags(DWORD, [
    "D3DPTEXTURECAPS_PERSPECTIVE",
    "D3DPTEXTURECAPS_POW2",
    "D3DPTEXTURECAPS_ALPHA",
    "D3DPTEXTURECAPS_SQUAREONLY",
    "D3DPTEXTURECAPS_TEXREPEATNOTSCALEDBYSIZE",
    "D3DPTEXTURECAPS_ALPHAPALETTE",
    "D3DPTEXTURECAPS_NONPOW2CONDITIONAL",
    "D3DPTEXTURECAPS_PROJECTED",
    "D3DPTEXTURECAPS_CUBEMAP",
    "D3DPTEXTURECAPS_VOLUMEMAP",
    "D3DPTEXTURECAPS_MIPMAP",
    "D3DPTEXTURECAPS_MIPVOLUMEMAP",
    "D3DPTEXTURECAPS_MIPCUBEMAP",
    "D3DPTEXTURECAPS_CUBEMAP_POW2",
    "D3DPTEXTURECAPS_VOLUMEMAP_POW2",
    "D3DPTEXTURECAPS_NOPROJECTEDBUMPENV",
])

D3DPTFILTERCAPS = Flags(DWORD, [
    "D3DPTFILTERCAPS_MINFPOINT",
    "D3DPTFILTERCAPS_MINFLINEAR",
    "D3DPTFILTERCAPS_MINFANISOTROPIC",
    "D3DPTFILTERCAPS_MINFPYRAMIDALQUAD",
    "D3DPTFILTERCAPS_MINFGAUSSIANQUAD",
    "D3DPTFILTERCAPS_MIPFPOINT",
    "D3DPTFILTERCAPS_MIPFLINEAR",
    "D3DPTFILTERCAPS_CONVOLUTIONMONO",
    "D3DPTFILTERCAPS_MAGFPOINT",
    "D3DPTFILTERCAPS_MAGFLINEAR",
    "D3DPTFILTERCAPS_MAGFANISOTROPIC",
    "D3DPTFILTERCAPS_MAGFPYRAMIDALQUAD",
    "D3DPTFILTERCAPS_MAGFGAUSSIANQUAD",
])

D3DPTADDRESSCAPS = Flags(DWORD, [
    "D3DPTADDRESSCAPS_WRAP",
    "D3DPTADDRESSCAPS_MIRROR",
    "D3DPTADDRESSCAPS_CLAMP",
    "D3DPTADDRESSCAPS_BORDER",
    "D3DPTADDRESSCAPS_INDEPENDENTUV",
    "D3DPTADDRESSCAPS_MIRRORONCE",
])

D3DSTENCILCAPS = Flags(DWORD, [
    "D3DSTENCILCAPS_KEEP",
    "D3DSTENCILCAPS_ZERO",
    "D3DSTENCILCAPS_REPLACE",
    "D3DSTENCILCAPS_INCRSAT",
    "D3DSTENCILCAPS_DECRSAT",
    "D3DSTENCILCAPS_INVERT",
    "D3DSTENCILCAPS_INCR",
    "D3DSTENCILCAPS_DECR",
    "D3DSTENCILCAPS_TWOSIDED",
])

D3DTEXOPCAPS = Flags(DWORD, [
    "D3DTEXOPCAPS_DISABLE",
    "D3DTEXOPCAPS_SELECTARG1",
    "D3DTEXOPCAPS_SELECTARG2",
    "D3DTEXOPCAPS_MODULATE",
    "D3DTEXOPCAPS_MODULATE2X",
    "D3DTEXOPCAPS_MODULATE4X",
    "D3DTEXOPCAPS_ADD",
    "D3DTEXOPCAPS_ADDSIGNED",
    "D3DTEXOPCAPS_ADDSIGNED2X",
    "D3DTEXOPCAPS_SUBTRACT",
    "D3DTEXOPCAPS_ADDSMOOTH",
    "D3DTEXOPCAPS_BLENDDIFFUSEALPHA",
    "D3DTEXOPCAPS_BLENDTEXTUREALPHA",
    "D3DTEXOPCAPS_BLENDFACTORALPHA",
    "D3DTEXOPCAPS_BLENDTEXTUREALPHAPM",
    "D3DTEXOPCAPS_BLENDCURRENTALPHA",
    "D3DTEXOPCAPS_PREMODULATE",
    "D3DTEXOPCAPS_MODULATEALPHA_ADDCOLOR",
    "D3DTEXOPCAPS_MODULATECOLOR_ADDALPHA",
    "D3DTEXOPCAPS_MODULATEINVALPHA_ADDCOLOR",
    "D3DTEXOPCAPS_MODULATEINVCOLOR_ADDALPHA",
    "D3DTEXOPCAPS_BUMPENVMAP",
    "D3DTEXOPCAPS_BUMPENVMAPLUMINANCE",
    "D3DTEXOPCAPS_DOTPRODUCT3",
    "D3DTEXOPCAPS_MULTIPLYADD",
    "D3DTEXOPCAPS_LERP",
])

D3DFVFCAPS = Flags(DWORD, [
    "D3DFVFCAPS_TEXCOORDCOUNTMASK",
    "D3DFVFCAPS_DONOTSTRIPELEMENTS",
    "D3DFVFCAPS_PSIZE",
])

D3DVTXPCAPS = Flags(DWORD, [
    "D3DVTXPCAPS_TEXGEN",
    "D3DVTXPCAPS_MATERIALSOURCE7",
    "D3DVTXPCAPS_DIRECTIONALLIGHTS",
    "D3DVTXPCAPS_POSITIONALLIGHTS",
    "D3DVTXPCAPS_LOCALVIEWER",
    "D3DVTXPCAPS_TWEENING",
    "D3DVTXPCAPS_TEXGEN_SPHEREMAP",
    "D3DVTXPCAPS_NO_TEXGEN_NONLOCALVIEWER",
])

D3DDEVCAPS2 = Flags(DWORD, [
    "D3DDEVCAPS2_STREAMOFFSET",
    "D3DDEVCAPS2_DMAPNPATCH",
    "D3DDEVCAPS2_ADAPTIVETESSRTPATCH",
    "D3DDEVCAPS2_ADAPTIVETESSNPATCH",
    "D3DDEVCAPS2_CAN_STRETCHRECT_FROM_TEXTURES",
    "D3DDEVCAPS2_PRESAMPLEDDMAPNPATCH",
    "D3DDEVCAPS2_VERTEXELEMENTSCANSHARESTREAMOFFSET",
])

D3DDTCAPS = Flags(DWORD, [
    "D3DDTCAPS_UBYTE4",
    "D3DDTCAPS_UBYTE4N",
    "D3DDTCAPS_SHORT2N",
    "D3DDTCAPS_SHORT4N",
    "D3DDTCAPS_USHORT2N",
    "D3DDTCAPS_USHORT4N",
    "D3DDTCAPS_UDEC3",
    "D3DDTCAPS_DEC3N",
    "D3DDTCAPS_FLOAT16_2",
    "D3DDTCAPS_FLOAT16_4",
])

#D3DPS_VERSION = Enum("DWORD", [
#    "D3DPS_VERSION(0,0)",
#    "D3DPS_VERSION(1,0)",
#    "D3DPS_VERSION(1,1)",
#    "D3DPS_VERSION(1,2)",
#    "D3DPS_VERSION(1,3)",
#    "D3DPS_VERSION(1,4)",
#    "D3DPS_VERSION(2,0)",
#    "D3DPS_VERSION(3,0)",
#])
D3DPS_VERSION = DWORD

#D3DVS_VERSION = Enum("DWORD", [
#    "D3DVS_VERSION(0,0)",
#    "D3DVS_VERSION(1,0)",
#    "D3DVS_VERSION(1,1)",
#    "D3DVS_VERSION(2,0)",
#    "D3DVS_VERSION(3,0)",
#])
D3DVS_VERSION = DWORD

D3DCAPS9 = Struct("D3DCAPS9", [
    (D3DDEVTYPE, "DeviceType"),
    (UINT, "AdapterOrdinal"),
    (D3DCAPS, "Caps"),
    (D3DCAPS2, "Caps2"),
    (D3DCAPS3, "Caps3"),
    (D3DPRESENT_INTERVAL, "PresentationIntervals"),
    (D3DCURSORCAPS, "CursorCaps"),
    (D3DDEVCAPS, "DevCaps"),
    (D3DPMISCCAPS, "PrimitiveMiscCaps"),
    (D3DPRASTERCAPS, "RasterCaps"),
    (D3DPCMPCAPS, "ZCmpCaps"),
    (D3DPBLENDCAPS, "SrcBlendCaps"),
    (D3DPBLENDCAPS, "DestBlendCaps"),
    (D3DPCMPCAPS, "AlphaCmpCaps"),
    (D3DPSHADECAPS, "ShadeCaps"),
    (D3DPTEXTURECAPS, "TextureCaps"),
    (D3DPTFILTERCAPS, "TextureFilterCaps"),
    (D3DPTFILTERCAPS, "CubeTextureFilterCaps"),
    (D3DPTFILTERCAPS, "VolumeTextureFilterCaps"),
    (D3DPTADDRESSCAPS, "TextureAddressCaps"),
    (D3DPTADDRESSCAPS, "VolumeTextureAddressCaps"),
    (D3DLINECAPS, "LineCaps"),
    (DWORD, "MaxTextureWidth"),
    (DWORD, "MaxTextureHeight"),
    (DWORD, "MaxVolumeExtent"),
    (DWORD, "MaxTextureRepeat"),
    (DWORD, "MaxTextureAspectRatio"),
    (DWORD, "MaxAnisotropy"),
    (Float, "MaxVertexW"),
    (Float, "GuardBandLeft"),
    (Float, "GuardBandTop"),
    (Float, "GuardBandRight"),
    (Float, "GuardBandBottom"),
    (Float, "ExtentsAdjust"),
    (D3DSTENCILCAPS, "StencilCaps"),
    (D3DFVFCAPS, "FVFCaps"),
    (D3DTEXOPCAPS, "TextureOpCaps"),
    (DWORD, "MaxTextureBlendStages"),
    (DWORD, "MaxSimultaneousTextures"),
    (D3DVTXPCAPS, "VertexProcessingCaps"),
    (DWORD, "MaxActiveLights"),
    (DWORD, "MaxUserClipPlanes"),
    (DWORD, "MaxVertexBlendMatrices"),
    (DWORD, "MaxVertexBlendMatrixIndex"),
    (Float, "MaxPointSize"),
    (DWORD, "MaxPrimitiveCount"),
    (DWORD, "MaxVertexIndex"),
    (DWORD, "MaxStreams"),
    (DWORD, "MaxStreamStride"),
    (D3DVS_VERSION, "VertexShaderVersion"),
    (DWORD, "MaxVertexShaderConst"),
    (D3DPS_VERSION, "PixelShaderVersion"),
    (Float, "PixelShader1xMaxValue"),
    (D3DDEVCAPS2, "DevCaps2"),
    (Float, "MaxNpatchTessellationLevel"),
    (DWORD, "Reserved5"),
    (UINT, "MasterAdapterOrdinal"),
    (UINT, "AdapterOrdinalInGroup"),
    (UINT, "NumberOfAdaptersInGroup"),
    (D3DDTCAPS, "DeclTypes"),
    (DWORD, "NumSimultaneousRTs"),
    (D3DPTFILTERCAPS, "StretchRectFilterCaps"),
    (D3DVSHADERCAPS2_0, "VS20Caps"),
    (D3DPSHADERCAPS2_0, "PS20Caps"),
    (D3DPTFILTERCAPS, "VertexTextureFilterCaps"),
    (DWORD, "MaxVShaderInstructionsExecuted"),
    (DWORD, "MaxPShaderInstructionsExecuted"),
    (DWORD, "MaxVertexShader30InstructionSlots"),
    (DWORD, "MaxPixelShader30InstructionSlots"),
])

