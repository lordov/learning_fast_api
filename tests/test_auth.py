import pytest
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import Role
from tests.conftest import client, async_session_maker


@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:
        session: AsyncSession
        stmt = insert(Role).values(id=1, name="admin", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(Role)
        result = await session.execute(query)
        roles = result.scalars().all()
        for role in roles:
            print(
                f"ID: {role.id}, Name: {role.name}, Permissions: {role.permissions}")

        # Проверка, что данные корректны
        assert len(roles) == 1
        assert roles[0].id == 1
        assert roles[0].name == "admin"
        assert roles[0].permissions is None


def test_register():
    response = client.post("/auth/register", json={
        "email": "user@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
    }
    )
    assert response.status_code == 201
