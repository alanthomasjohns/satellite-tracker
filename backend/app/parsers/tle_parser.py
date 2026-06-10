from app.domain.tle import TLERecord


class TLEParser:
    def parse_records(self, raw_tle: str) -> list[TLERecord]:
        lines = raw_tle.strip().splitlines()
        satellites = []

        for i in range(0, len(lines), 3):
            satellites.append(
                TLERecord(
                    name=lines[i],
                    line1=lines[i + 1],
                    line2=lines[i + 2],
                )
            )

        return satellites