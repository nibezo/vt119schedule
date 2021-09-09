from vkwave.bots import BaseEvent
from vkwave.bots.core.dispatching.filters import base, builtin

import filter


class IdCheck(base.BaseFilter):
    idlist = filter.convert_id('id219.txt')  # convert id from the file to the list "idlist"

    async def check(self, event: BaseEvent) -> base.FilterResult:
        return base.FilterResult(event.object.object.message.from_id in self.idlist)
