# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc
from typing import (Any, Dict, Optional, Tuple)

from erniebot.response import EBResponse
from erniebot.types import (ParamsType, HeadersType)
from .protocol import Resource


class Cancellable(Resource):
    """Cancellable resource."""

    @classmethod
    def cancel(cls, **kwargs: Any) -> EBResponse:
        """Cancel a long-running operation."""
        config = kwargs.pop('_config_', {})
        resource = cls.new_object(**config)
        cancel_kwargs = kwargs
        return resource.cancel_resource(**cancel_kwargs)

    @classmethod
    async def acancel(cls, **kwargs: Any) -> EBResponse:
        """Asynchronous version of `cancel`."""
        config = kwargs.pop('_config_', {})
        resource = cls.new_object(**config)
        cancel_kwargs = kwargs
        resp = await resource.acancel_resource(**cancel_kwargs)
        return resp

    def cancel_resource(self, **cancel_kwargs: Any) -> EBResponse:
        path, params, headers, request_timeout = self._prepare_cancel(
            cancel_kwargs)
        resp = self.request(
            method='POST',
            path=path,
            params=params,
            stream=False,
            headers=headers,
            request_timeout=request_timeout)
        resp = self._postprocess_cancel(resp)
        return resp

    async def acancel_resource(self, **cancel_kwargs: Any) -> EBResponse:
        path, params, headers, request_timeout = self._prepare_cancel(
            cancel_kwargs)
        resp = await self.arequest(
            method='POST',
            path=path,
            params=params,
            stream=False,
            headers=headers,
            request_timeout=request_timeout)
        resp = self._postprocess_cancel(resp)
        return resp

    @abc.abstractmethod
    def _prepare_cancel(self,
                        kwargs: Dict[str, Any]) -> Tuple[str,
                                                         Optional[ParamsType],
                                                         Optional[HeadersType],
                                                         Optional[float],
                                                         ]:
        ...

    def _postprocess_cancel(self, resp: EBResponse) -> EBResponse:
        return resp
