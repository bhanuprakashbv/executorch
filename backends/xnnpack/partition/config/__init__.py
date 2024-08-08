# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from typing import List, Type

from executorch.backends.xnnpack.partition.config.gemm_configs import (
    AddmmConfig,
    ConvolutionConfig,
    LinearConfig,
)

from executorch.backends.xnnpack.partition.config.generic_node_configs import (
    AbsConfig,
    AddConfig,
    AvgPoolingConfig,
    CatConfig,
    CeilConfig,
    ClampConfig,
    ConstantPadConfig,
    DeQuantizedPerTensorConfig,
    DivConfig,
    FloorConfig,
    HardswishConfig,
    # EluConfig,
    HardtanhConfig,
    LeakyReLUConfig,
    MaximumConfig,
    MaxPool2dConfig,
    MeanDimConfig,
    MinimumConfig,
    MulConfig,
    NegConfig,
    PermuteConfig,
    PowConfig,
    QuantizedPerTensorConfig,
    ReLUConfig,
    SigmoidConfig,
    SliceCopyConfig,
    SoftmaxConfig,
    SquareRootConfig,
    SubConfig,
    UpsampleBilinear2dConfig,
)
from executorch.backends.xnnpack.partition.config.node_configs import (
    BatchNormConfig,
    MaxDimConfig,
    PreluConfig,
)
from executorch.backends.xnnpack.partition.config.xnnpack_config import (
    XNNPartitionerConfig,
)

ALL_PARTITIONER_CONFIGS: List[Type[XNNPartitionerConfig]] = [
    AbsConfig,
    AddConfig,
    AddmmConfig,
    AvgPoolingConfig,
    BatchNormConfig,
    CatConfig,
    CeilConfig,
    ConstantPadConfig,
    ConvolutionConfig,
    ClampConfig,
    DivConfig,
    # EluConfig, # Waiting for PyTorch Pin Update
    FloorConfig,
    HardtanhConfig,
    HardswishConfig,
    LeakyReLUConfig,
    LinearConfig,
    MaxDimConfig,
    MaximumConfig,
    MaxPool2dConfig,
    MeanDimConfig,
    MinimumConfig,
    MulConfig,
    NegConfig,
    PermuteConfig,
    PowConfig,
    PreluConfig,
    ReLUConfig,
    SigmoidConfig,
    SliceCopyConfig,
    SoftmaxConfig,
    SquareRootConfig,
    SubConfig,
    UpsampleBilinear2dConfig,
    # Quant/Dequant Op Configs
    QuantizedPerTensorConfig,
    DeQuantizedPerTensorConfig,
]
